# Goal: Print the media type based on a file name's extension

# Given: The user enters a file name
# Find: The matching media type

# Step 1: Ask the user for a file name, clean it, and store it
filename = input("File name: ").strip().lower()

# Step 2: If the file name ends with ".gif", print "image/gif"
if filename.endswith(".gif"):
    print("image/gif")

# Step 3: Else if the file name ends with ".jpg" or ".jpeg", print "image/jpeg"
elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
    print("image/jpeg")

# Step 4: Else if the file name ends with".png", print "image/png"
elif filename.endswith(".png"):
    print("image/png")

# Step 5: else if the file name ends with ".pdf", print "application/pdf"
elif filename.endswith(".pdf"):
    print("application/pdf")

# Step 6: else if the file name ends with ".txt", print "text/plain"
elif filename.endswith(".txt"):
    print("text/plain")

# Step 7: else if the file name ends with ".zip", print "application/zip"
elif filename.endswith(".zip"):
    print("application/zip")

# Step 8: Otherwise, print "application/octet-stream"
else:
    print("application/octet-stream")

