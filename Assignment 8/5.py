def compress(chars):
    write_index = 0
    count = 1

    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            count += 1
        else:
            chars[write_index] = chars[i - 1]
            write_index += 1

            if count > 1:
                count_str = str(count)
                chars[write_index:write_index + len(count_str)] = list(count_str)
                write_index += len(count_str)

            count = 1

    chars[write_index] = chars[-1]
    write_index += 1

    if count > 1:
        count_str = str(count)
        chars[write_index:write_index + len(count_str)] = list(count_str)
        write_index += len(count_str)

    return write_index


chars = ["a", "a", "b", "b", "c", "c", "c"]
new_length = compress(chars)
print(new_length)
print(chars[:new_length])
