def save_file(filename: str, data):
    filename = "data/" + filename
    try:
        with open(filename, 'w') as f:
            f.write(str(data))
            f.close()
            return True
    except:
        return False


if __name__ == "__main__":
    save_file('id.txt', 211233)
