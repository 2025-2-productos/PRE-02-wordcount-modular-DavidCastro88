# obtain a list of files in the input directory
import os

def read_all_lines():
    all_lines = []
    input_files_list = os.listdir("data/input/")
    for filename in input_files_list:
        with open("data/input/"+filename,"r",encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)
    return all_lines

def write_count_words(counter):
    # create the directory output/ if it doesn't exist
    if not os.path.exists("data/output"):
        os.makedirs("data/output")

    # save the results using tsv format
    with open("data/output/results.tsv", "w", encoding="utf-8") as f:
        for key, value in counter.items():
            # write the key and value to the file
            f.write(f"{key}\t{value}\n")


def main():
    ### Listamos los archivos
    #all_lines = read_all_lines()
    input_files_list = os.listdir("data/input/")

    # count the frequency of the words in the files in the input directory
    counter = {}
    for filename in input_files_list:
        with open("data/input/" + filename) as f:
            for l in f:
                for w in l.split():
                    w = w.lower().strip(",.!?")
                    counter[w] = counter.get(w, 0) + 1
                    
    write_count_words(counter)                 
                  
                    



if __name__ == "__main__":
    main()
