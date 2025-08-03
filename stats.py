def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents   

     
def count_words(file_contents):
    words_list = file_contents.split()
    return len(words_list)

def char_count(content):
    lowered, final = content.lower(), {}
    for _ in lowered:
        if _ in final:
            final[_] += 1
        else:
            final[_] = 1
    return final

def num_char_count(count_dict):
    final_res = [{"char": key, "num": value} for key, value in count_dict.items()]
    final_res.sort(reverse=True, key=lambda x: x["num"])
    return final_res

