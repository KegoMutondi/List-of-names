def main():
    # Prompt the user to enter names separated by commas
    names_input = input("Enter a list of names, separated by commas: ")
    
    # Split the input string into a list of names
    names_list = [name.strip() for name in names_input.split(",")]
    
    # Count the total number of names entered (including duplicates)
    total_names_count = len(names_list)
    
    # Remove duplicates by converting the list to a set, then back to a list
    unique_names_list = list(set(names_list))
    
    # Sort the unique names list alphabetically
    unique_names_list.sort()
    
    # Print the sorted list of names
    print("Sorted list of names (without duplicates):")
    for name in unique_names_list:
        print(name)
    
    # Print the total number of names entered by the user
    print(f"\nTotal number of names entered (including duplicates): {total_names_count}")

if __name__ == "__main__":
    main()
