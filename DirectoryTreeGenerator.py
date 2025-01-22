import os

def main():
    current_directory = input("Input the absolute file path: ").strip().replace("\\", "/")
    filter_list = ['.git', '__pycache__', '.idea']

    if not os.path.exists(current_directory):
        print("The provided path does not exist. Please check and try again.")
        return

    print("Directory Tree:")
    generate_tree(current_directory, filter_list)

def generate_tree(path, filter_list, level=0, is_last=False):
    base_name = os.path.basename(path)
    
    if base_name in filter_list:
        return
  
    indent = "    " * level + ("└── " if is_last else "├── ") if level > 0 else ""
    print(f"{indent}{base_name}")
    
    if os.path.isdir(path):
        sub_items = os.listdir(path)
        sub_items.sort()
        for idx, item in enumerate(sub_items):
            is_last_item = (idx == len(sub_items) - 1)
            generate_tree(os.path.join(path, item), filter_list, level + 1, is_last_item)

if __name__ == "__main__":
    main()
    
