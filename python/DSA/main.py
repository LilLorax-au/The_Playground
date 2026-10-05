from data_structs import Stack



def main():
    test_stack()

    return 0

def test_stack():
    plates = Stack()

    for i in range(10):
        plates.push(f"plate_{i}")
        print(plates.top())
    
    for i in range(11):
        try:
            print(plates.pop())
        except IndexError as e:
            print(e.args[0])


if __name__ == "__main__":
    main()


