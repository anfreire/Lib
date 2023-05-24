#ifndef HEADER_HPP
# define HEADER_HPP


/*			Printing Colors				*/
# define	RESET		        "\033[0m"
# define	COLOR_RED	        "\033[1;31m"
# define	COLOR_GREEN	        "\033[1;32m"
# define	COLOR_YELLOW		"\033[1;33m"
# define	COLOR_BLUE          "\033[1;34m"
# define	COLOR_MAGENTA		"\033[1;35m"
# define	COLOR_CYAN          "\033[1;36m"
# define	COLOR_WHITE	        "\033[1;37m"
# define	BACKGROUND_RED		"\033[1;41m"
# define	BACKGROUND_GREEN	"\033[1;42m"
# define	BACKGROUND_YELLOW	"\033[1;43m"
# define	BACKGROUND_BLUE		"\033[1;44m"
# define	BACKGROUND_MAGENTA	"\033[1;45m"
# define	BACKGROUND_CYAN		"\033[1;46m"
# define	BACKGROUND_WHITE	"\033[1;47m"
# define	BACKGROUND_BLACK	"\033[1;48m"


/*				Types					*/
typedef		unsigned char		t_uchar;
typedef		unsigned short		t_ushort;
typedef		unsigned int		t_uint;
typedef		unsigned long		t_ulong;
typedef		unsigned long long	t_ullong;


/*				Constants				*/
# define	PI					3.1415926535897932384626433832795028841971693993751058209749445923078164062
# define	E					2.7182818284590452353602874713526624977572470936999595749669676277240766303
# define	INF					std::numeric_limits<double>::infinity()
# define	NAN					std::numeric_limits<double>::quiet_NaN()
# define	EPSILON				std::numeric_limits<double>::epsilon()
# define	MAX_CHAR			std::numeric_limits<char>::max()
# define	MIN_CHAR			std::numeric_limits<char>::min()
# define	MAX_INT				std::numeric_limits<int>::max()
# define	MIN_INT				std::numeric_limits<int>::min()
# define	MAX_FLOAT			std::numeric_limits<float>::max()
# define	MIN_FLOAT			std::numeric_limits<float>::min()
# define	MAX_DOUBLE			std::numeric_limits<double>::max()
# define	MIN_DOUBLE			std::numeric_limits<double>::min()
# define	MAX_INT				std::numeric_limits<int>::max()
# define	MIN_INT				std::numeric_limits<int>::min()
# define	MAX_LONG			std::numeric_limits<long>::max()
# define	MIN_LONG			std::numeric_limits<long>::min()
# define	MAX_LONGLONG		std::numeric_limits<long long>::max()
# define	MIN_LONGLONG		std::numeric_limits<long long>::min()


/*				Functions				*/
# define	ABS(x)				((x) < 0 ? -(x) : (x))
# define	MIN(x, y)			((x) < (y) ? (x) : (y))
# define	MAX(x, y)			((x) > (y) ? (x) : (y))
# define	SWAP(x, y)			((x) ^= (y) ^= (x) ^= (y))
# define	ISDIGIT(x)			((x) >= '0' && (x) <= '9')
# define	ISALPHA(x)			(((x) >= 'a' && (x) <= 'z') || ((x) >= 'A' && (x) <= 'Z'))
# define	ISUPPER(x)			((x) >= 'A' && (x) <= 'Z')
# define	ISLOWER(x)			((x) >= 'a' && (x) <= 'z')
# define	ISPRINT(x)			((x) >= 32 && (x) <= 126)
# define	ISASCII(x)			((x) >= 0 && (x) <= 127)
# define	TOUPPER(x)			((x) >= 'a' && (x) <= 'z' ? (x) - 32 : (x))
# define	TOLOWER(x)			((x) >= 'A' && (x) <= 'Z' ? (x) + 32 : (x))
# define	TOINT(x)			((x) - '0')
# define	TOCHAR(x)			((x) + '0')


/*				Libraries				*/
# include 	<cmath>
# include 	<cstdlib>
# include 	<iomanip>
# include 	<iostream>
# include 	<limits>
# include 	<sstream>
# include 	<string>
# include 	<cstring>

// ...


#endif
