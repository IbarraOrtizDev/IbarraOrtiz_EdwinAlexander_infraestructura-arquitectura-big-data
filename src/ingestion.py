from utils.crashData import crash_data
from utils.fetchData import FetchData
from utils.fileOperator import FileOperator
from utils.manageDB import ManageDB


def main():
    # Fetch data from API
    dataClass = FetchData()
    data = dataClass.fetch()

    dataExport = crash_data(dataClass.fetch_zip())

    manageDB = ManageDB()
    manageDB.insert_users_batch(data)
    manageDB.insert_ventas_batch(dataExport)

    manageFile = FileOperator()

    # Write data to excel
    manageFile.writeExcel(dataExport)
    # Generate audit file
    manageFile.generateAuditFile(dataExport)

if __name__ == '__main__':
    main()