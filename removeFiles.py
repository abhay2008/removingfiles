import os
import shutil
import time

def main():
	deleted_folders_count = 0
	deleted_files_count = 0

	path = "/PATH_TO_DELETE"

	days = 30

	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):
		for root_folder, folders, files in os.walk(path):
			if seconds >= get_age(root_folder):
				rm_folder(root_folder)
				deleted_folders_count += 1
				break

			else:
				for folder in folders:
					folder_path = os.path.join(root_folder, folder)
					if seconds >= get_age(folder_path):
						rm_folder(folder_path)
						deleted_folders_count += 1
				for file in files:
					file_path = os.path.join(root_folder, file)

					if seconds >= get_age(file_path):
						rm_file(file_path)
						deleted_files_count += 1

		else:
			if seconds >= get_age(path):
				rm_file(path)
				deleted_files_count += 1

	else:
		print(f'"{path}" is not found')
		deleted_files_count += 1

	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")


def rm_folder(path):
	if not shutil.rmtree(path):
		print(f"{path} is removed successfully")

	else:
		print(f"Unable to delete the "+path)



def rm_file(path):
	if not os.remove(path):
		print(f"{path} is removed successfully")

	else:
		print("Unable to delete the "+path)


def get_age(path):
	ctime = os.stat(path).st_ctime
	return ctime


if __name__ == '__main__':
	main()
