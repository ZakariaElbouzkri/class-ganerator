import sys

def	wrieTemp(temp, fileName):
	with open(fileName, 'w') as f:
		print(temp, file=f)
		f.close()

if (len(sys.argv) < 1):
	print("Pass className as args", file=sys.stderr)
	sys.exit(1)
className = sys.argv[1]


# Makfile template

Makefile = f"""NAME = {className}
CC   = g++ -Wall -Wextra -Werror -std=c++98
SRC  = main.cpp {className}.cpp
INC  = {className}.hpp
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

# className.cpp template

cppFile = f"""#include "{className}.hpp"\n\n
{className}::{className}( void ){{
	std::cout << "Default constructor called\\n";
}}\n
{className}::~{className}( void ){{
	std::cout << "Destructor called\\n";
}}\n
{className}::{className}( {className} const& rhs ){{
	std::cout << "Copy constructor called\\n";
	*this = rhs;
}}\n
{className}&	{className}::operator=( const {className}& rhs ){{
	std::cout << "Copy assignment operator called\\n";
	if (this != &rhs){{\n
	}}
	return (*this);
}}"""

# className.hpp template

hppFile = f"""#ifndef _{className}_HPP_
#define _{className}_HPP_\n
#include <iostream>\n
class	{className}{{\n
	private:\n
	public:
		{className}( void );
		~{className}( void );
		{className}( {className} const& rhs );
		{className}&	operator=( const {className}& rhs );
}};\n
#endif"""

mainFile = f"""#include "{className}.hpp"\n\n
int	main(){{
	std::cout << "hello world\\n";
	return (0);
}}"""

wrieTemp(Makefile, "Makefile")
wrieTemp(mainFile, "main.cpp")
wrieTemp(cppFile, f"{className}.cpp")
wrieTemp(hppFile, f"{className}.hpp")