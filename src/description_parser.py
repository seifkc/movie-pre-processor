import text_parsing_functions as tpf

def load_movie_description(filepath='data/train_to_busan_description.txt'):
  with open(filepath, "r", encoding="utf-8") as f:
    movie_string = f.read()

  return movie_string

def write_edited_movie_description(filepath, content):
    try:
        with open(filepath, 'w') as file:
            file.write(content)

    except(FileNotFoundError):
        print("File not found.")


if __name__ == '__main__':
  name_set = {"seokwoo", "sanghwa", "yongguk", "ingil", "jongil", "yonsuk", "jinhee", "suan", "seongkyeong", "jonggil"}
  replacement_value = "johnny5"
  stop_words = tpf.load_stopwords()
  movie_string = load_movie_description()

  clean_text = tpf.line_cleaning_pipeline(movie_string, stop_words, name_set, replacement_value)

  write_edited_movie_description('data/movie_parsed.txt', clean_text)