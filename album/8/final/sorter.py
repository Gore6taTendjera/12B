with open('numbers.txt', 'w') as f:
    for i in range(1, 126):
        f.write(f'<a href="album/8/final/{i}.webp"></a>\n')