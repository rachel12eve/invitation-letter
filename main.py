#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#save the name in the name list
with open("input/Names/invited_names.txt", "r") as name_list:
    names=name_list.readlines()

#save the content of template
with open("input/Letters/startubg_letter.txt","r+") as template:
    new_letter=template.read()

#replace the name and save to a new letter
for n in names:
    name=n.strip("\n")
    file_saved=f"output/ReadyToSend/invitation_to_{name}.txt"
    with open(file_saved,"w") as saved:
        new = new_letter.replace("[name]", name)
        saved.write(new)


