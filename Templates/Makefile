# ------------------------------------------------------------------------------------ EDIT HERE ------------------------------------------------------------------------------------ # 

NAME = # add executable name here


SRCS = # add source files here


VALGRIND_ARGS = # add valgrind arguments here if needed

# -------------------------------------------------------------------------------------- INFO --------------------------------------------------------------------------------------- #

#	Flags:
#
#	> Wall: - - - - - - - - turns on most, but not all, compiler warnings
#	> Wextra: - - - - - - - enables some extra warning flags that are not enabled by -Wall
#	> Werror: - - - - - - - treats all warnings as errors
#	> std=c++98:  - - - - - sets the C++ standard to C++98
#	> g:  - - - - - - - - - produces debugging information
#	> fsanitize=address:  - turns on address sanitizer


#	Rules:
#
#	> make: - - - - - - - - compiles the program
#	> make clean: - - - - - removes all object files
#	> make fclean:  - - - - removes all object files and the executable
#	> make re:  - - - - - - removes all object files and the executable, then compiles the program
#	> make check_leaks: - - recompiles the program without -fsanitize=address and runs valgrind to check for memory leaks


# --------------------------------------------------------------------------- DO NOT EDIT BELOW THIS LINE --------------------------------------------------------------------------- #

OK= [ \033[1;32mOK\033[0m ]
FAIL= [ \033[1;31mFAILED\033[0m ]
WARN= [ \033[1;33mWARNING\033[0m ]
WHITE= \033[1;37m
RESET= \033[0m

SRCS_DIR = ./src/

OBJS_DIR = ./obj/

all: $(NAME)

CC = @c++

CFLAGS = -Wall -Wextra -Werror -std=c++98 -g -fsanitize=address

OBJS = $(addprefix $(OBJS_DIR), $(SRCS:.cpp=.o))

$(OBJS_DIR)%.o: $(SRCS_DIR)%.cpp
	@mkdir -p $(OBJS_DIR)
	@$(CC) $(CFLAGS) -c $< -o $@
	@if [ -f $@ ]; then echo "$(OK) Object file created successfully: $(WHITE)$@$(RESET)"; else echo "$(FAIL) Object file creation failed: $(WHITE)$@$(RESET)"; fi

$(NAME): $(OBJS)
	@$(CC) $(CFLAGS) $(OBJS) -o $(NAME)
	@if [ -f $(NAME) ]; then echo "$(OK) Executable file created successfully: $(WHITE)$(NAME)$(RESET)"; else echo "$(FAIL) Executable file creation failed: $(WHITE)$(NAME)$(RESET)"; fi

clean:
	@for file in $(OBJS); do \
		if [ -f $$file ]; then \
			rm $$file; \
			if [ ! -f $$file ]; then echo "$(OK) Object file deleted successfully: $(WHITE)$$file$(RESET)"; else echo "$(FAIL) Object file deletion failed: $(WHITE)$$file$(RESET)"; fi \
		fi \
	done


fclean: clean
	@rm -rf $(NAME)
	@if [ ! -f $(NAME) ]; then echo "$(OK) Executable file deleted successfully: $(WHITE)$(NAME)$(RESET)"; else echo "$(FAIL) Executable file deletion failed: $(WHITE)$(NAME)$(RESET)"; fi

re: fclean all

check_leaks:
	@echo "$(WARN) Recompiling without $(WHITE)-fsanitize=address$(RESET) to run valgrind"
	@$(MAKE) re CFLAGS="$(filter-out -fsanitize=address,$(CFLAGS))" NAME=$(NAME)
	@valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./$(NAME) $(VALGRIND_ARGS)

.PHONY: all clean fclean re

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #