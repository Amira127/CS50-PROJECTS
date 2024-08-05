name = input("File name: ").strip().title()
type =name[len(name)-4:len(name)]
match type:
    case ".Gif":
        print("image/gif")
    case ".Jpg" | "Jpeg":
        print("image/jpeg")
    case ".Png":
        print("image/png")
    case ".Pdf":
        print("application/pdf")
    case ".Txt":
        print("text/plain")
    case ".Zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
