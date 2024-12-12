import os

def main():
   file_count = 0
   folder_count = 0
   combined_content = ""
   current_dir = os.getcwd()
   
   output_filename = input("Enter output filename (or press Enter for default): ").strip()
   if not output_filename:
       output_filename = os.path.basename(current_dir) + "-code-collection.md"
   elif not output_filename.endswith('.md'):
       output_filename += '.md'
   
   print(f"Starting code-collector in: {current_dir}")
   
   for folder_name, subfolders, filenames in os.walk(current_dir):
       folder_count += len(subfolders)
       file_count += len(filenames)
       print(f"Processing folder: {folder_name}")
       
       for filename in filenames:
           try:
               with open(os.path.join(folder_name, filename), 'r') as file:
                   print(f"Reading file: {filename}")
                   combined_content += f"# {filename}\n\n```\n{file.read()}\n```\n\n"
           except:
               print(f"ERROR: Could not read {filename}")
   
   with open(output_filename, 'w') as output:
       output.write(f"# Code Collection\n\nFiles: {file_count}\nFolders: {folder_count}\n\n")
       output.write(combined_content)
   
   print(f"\nCollection complete!")
   print(f"Total files processed: {file_count}")
   print(f"Total folders found: {folder_count}")
   print(f"Output written to: {output_filename}")

if __name__ == "__main__":
   main()