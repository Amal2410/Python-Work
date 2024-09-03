def is_anagram(word1,word2):

    return sorted(word1)==sorted(word2)

source_word="listen"

target_word="silent"

print(is_anagram(source_word,target_word))