import logging

logging.basicConfig(filename="security.log",
    level=logging.INFO, filemode="w", encoding="utf-8",
    format="%(asctime)s %(levelname)-8s %(message)s")

users = ["dana", "avi", "dana", "noa"]
passwords = ["1234", "0000", "1111", "1234"]
successful = 0
failed = 0

for user, password in zip(users, passwords):
    if password != "1234":
        logging.warning(f"Wrong password for user {user}.")
        failed += 1
    else:
        logging.info(f"User {user} successfully logged in!")
        successful += 1

print(f"Successful: {successful}, failed: {failed}")