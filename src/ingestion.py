from fetchData import FetchData
from fileOperator import FileOperator
from manageDB import ManageDB


def main():
    # Fetch data from API
    dataClass = FetchData()
    data = dataClass.fetch()

    manageDB = ManageDB()
    manageDB.insert_users_batch(data)

    manageFile = FileOperator()

    # Write data to excel
    manageFile.writeExcel(data)
    # Generate audit file
    manageFile.generateAuditFile(data)

if __name__ == '__main__':
    main()