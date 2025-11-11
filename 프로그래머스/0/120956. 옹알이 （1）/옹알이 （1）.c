#include <stdio.h>
#include <stdbool.h>
#include <string.h>

static bool pronounceable(const char *s) {
    bool used_aya = false, used_ye = false, used_woo = false, used_ma = false;
    size_t i = 0, n = strlen(s);

    while (i < n) {
        switch (s[i]) {
            case 'a': // "aya"
                if (!used_aya && i + 3 <= n && strncmp(s + i, "aya", 3) == 0) {
                    used_aya = true; i += 3;
                } else return false;
                break;
            case 'y': // "ye"
                if (!used_ye && i + 2 <= n && strncmp(s + i, "ye", 2) == 0) {
                    used_ye = true; i += 2;
                } else return false;
                break;
            case 'w': // "woo"
                if (!used_woo && i + 3 <= n && strncmp(s + i, "woo", 3) == 0) {
                    used_woo = true; i += 3;
                } else return false;
                break;
            case 'm': // "ma"
                if (!used_ma && i + 2 <= n && strncmp(s + i, "ma", 2) == 0) {
                    used_ma = true; i += 2;
                } else return false;
                break;
            default:
                return false;
        }
    }
    return true; // 끝까지 정확히 분해됨
}

int solution(const char* babbling[], size_t babbling_len) {
    int answer = 0;
    for (size_t i = 0; i < babbling_len; ++i) {
        if (pronounceable(babbling[i])) ++answer;
    }
    return answer;
}
