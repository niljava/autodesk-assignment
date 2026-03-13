#include <string>
#include <cassert>
#include <algorithm>
#include <cctype>

std::string reverse_words(const std::string& str)
{
    std::string result = str;
    size_t word_start = std::string::npos;

    for (size_t i = 0; i <= result.size(); ++i)
    {
        if (i < result.size() && std::isalnum(static_cast<unsigned char>(result[i])))
        {
            if (word_start == std::string::npos)
                word_start = i;
        }
        else
        {
            if (word_start != std::string::npos)
            {
                std::reverse(result.begin() + word_start, result.begin() + i);
                word_start = std::string::npos;
            }
        }
    }

    return result;
}

int main()
{
    assert(reverse_words("String; 2be reversed...") == "gnirtS; eb2 desrever...");
    assert(reverse_words("Hello World") == "olleH dlroW");
    assert(reverse_words("abc123!") == "321cba!");
    assert(reverse_words("123 456") == "321 654");

    return 0;
}
