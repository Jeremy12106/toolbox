import os
import time

def main():
    folder_path = input("Enter the folder path: ").strip().replace("\\", "/")
    object_time = 'modify'  # choose 'creation' or'modify'

    # Confirm before renaming the files in the folder
    confirm = input(f"Are you sure you want to rename all files in '{folder_path}'? (y/n): ").strip().lower()
    
    if confirm == 'y':
        rename_files(folder_path, object_time)
    else:
        print("Operation canceled.")

def get_time(file_path, object_time):
    if object_time == 'creation':
        """
        Get the creation time of the file and return it in YYYYMMDD_HHMMSS format.
        """
        timestamp = os.path.getctime(file_path)
    elif object_time == 'modify':
        """
        Get the modify time of the file and return it in YYYYMMDD_HHMMSS format.
        """
        timestamp = os.path.getmtime(file_path)
    else:
        print("Invalid object time. Please choose 'creation' or'modify'.")
        return None

    return time.strftime('%Y%m%d_%H%M%S', time.localtime(timestamp))

def rename_files(folder_path, object_time):
    """
    Rename the files in the folder to their creation time.
    """
    if not os.path.exists(folder_path):
        print("The folder path does not exist!")
        return
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            creation_time = get_time(file_path, object_time)
            _, file_extension = os.path.splitext(filename)
            new_name = f"{creation_time}{file_extension}"
            new_path = os.path.join(folder_path, new_name)
            
            # Check if the file already exists, and modify the name if it does
            counter = 1
            while os.path.exists(new_path):
                new_name = f"{creation_time}_{counter}{file_extension}"
                new_path = os.path.join(folder_path, new_name)
                counter += 1
            
            try:
                os.rename(file_path, new_path)
                print(f"Renamed file '{filename}' to '{new_name}'")
            except Exception as e:
                print(f"Unable to rename file '{filename}': {e}")
                
if __name__ == "__main__":
    main()
