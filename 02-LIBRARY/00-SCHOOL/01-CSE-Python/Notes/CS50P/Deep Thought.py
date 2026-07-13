# Deep Thought

# Return "Yes" for 42 when asked a question

answer = input("Can you give me the answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
match answer:
    case "42":
        print("Yes")
    case "forty-two":
        print("Yes")
    case "forty two":
        print("Yes")
    case _:
        print("No")
