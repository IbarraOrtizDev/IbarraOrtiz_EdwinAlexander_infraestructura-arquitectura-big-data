from fetchData import FetchData
from fileOperator import FileOperator
from manageDB import ManageDB


def main():
    # Fetch data from API
    dataClass = FetchData()
    data = dataClass.fetch()

    dataExport = dataClass.fetch_zip()

    manageDB = ManageDB()
    manageDB.insert_users_batch(data)
    manageDB.insert_ventas_batch(dataExport)
    ventas = manageDB.fetch_all_ventas()

    manageFile = FileOperator()

    # Write data to excel
    manageFile.writeExcel(dataExport)
    # Generate audit file
    manageFile.generateAuditFile(dataExport)

if __name__ == '__main__':
    main()