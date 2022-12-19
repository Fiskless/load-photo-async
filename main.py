# zip -r photo.zip photo/*
# zip -r - photo/* > photo.zip


# import subprocess
#
# args = ['zip', '-r', '-', 'photo']
# archive = subprocess.Popen(args, stdout=subprocess.PIPE)
# stdout, stderr = archive.communicate()
# print(stdout)
#
# with open("archive.zip", "w+b") as file:
#     bytearray(file.write(stdout))

import asyncio


async def create_archive():
    args = ['zip', '-r', '-', 'photo']
    archive = await asyncio.create_subprocess_exec(
        *args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    while True:
        stdout = await archive.stdout.read(500*1024)
        with open("archive.zip", "a+b") as file:
            bytearray(file.write(stdout))
        if archive.stdout.at_eof():
            break


asyncio.run(create_archive())
