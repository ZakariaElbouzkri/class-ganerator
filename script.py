
import sys
import os

def	createTemplate(temp, fileName):
    if os.access(fileName, os.F_OK):
        return
    with open(fileName, 'w') as f:
        print(temp, file=f)
        f.close()

if (len(sys.argv) < 2):
	print("Pass cls as args", file=sys.stderr)
	sys.exit(1)

classes = sys.argv[1:]
mainClass = classes[0]

for cls in classes:
	# cls.cpp template
	cppFile = f"""#include "{cls}.hpp"\n\n
{cls}::{cls}( void )
{{
	std::cout << "Default constructor called\\n";
}}\n
{cls}::~{cls}( void )
{{
	std::cout << "Destructor called\\n";
}}\n
{cls}::{cls}( {cls} const& rhs )
{{
	std::cout << "Copy constructor called\\n";
	*this = rhs;
}}\n
{cls}&	{cls}::operator=( const {cls}& rhs )
{{
	std::cout << "Copy assignment operator called\\n";
	if (this != &rhs){{\n
	}}
	return (*this);
}}"""

	# cls.hpp template

	hppFile = f"""#ifndef _{cls}_HPP_
#define _{cls}_HPP_\n
#include <iostream>\n
class	{cls}
{{\n
	private:\n
	public:
		{cls}( void );
		~{cls}( void );
		{cls}( {cls} const& rhs );
		{cls}&	operator=( const {cls}& rhs );
}};\n
#endif"""

	createTemplate(cppFile, f"{cls}.cpp")
	createTemplate(hppFile, f"{cls}.hpp")

includes = [f'{cls}.hpp' for cls in classes]

files = [f'{cls}.cpp' for cls in classes]

mainFile = f"""#include "{mainClass}.hpp"\n\n
int	main()
{{
	std::cout << "hello world\\n";
	return (0);
}}"""

# Makfile template


# print(includes)

Makefile = f"""NAME = {mainClass}
CC   = g++ -Wall -Wextra -Werror -std=c++98
SRC  = main.cpp {" ".join(files)}
INC  = {" ".join(includes)}
RM   = rm -f
OBJ  = $(SRC:.cpp=.o)\n
all: $(NAME)\n
$(NAME): $(OBJ)
	$(CC) $^ -o $@\n
%.o: %.cpp $(INC)
	$(CC) -c $< -o $@\n
clean:
	$(RM) $(OBJ)\n
fclean: clean
	$(RM) $(NAME)\n
re: fclean all"""

createTemplate(Makefile, "Makefile")
createTemplate(mainFile, "main.cpp")
