
def save_result(result):

    with open("results.txt", "a") as file:
        file.write(str(result) + "\n")

    print("Result saved successfully!")


def read_results():

    try:
        with open("results.txt", "r") as file:
            print("\nSAVED RESULTS")
            print("-------------")
            print(file.read())

    except FileNotFoundError:
        print("No saved results found.")
