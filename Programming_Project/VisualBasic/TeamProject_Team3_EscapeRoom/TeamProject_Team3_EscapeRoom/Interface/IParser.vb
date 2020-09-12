Public Interface IParser

    Function FindElementByKey(key As String, value As String, ByRef element As DataElement) As Boolean
    Function FindElementByKey(key As String, value As String, dataList As List(Of DataElement), ByRef element As DataElement) As Boolean

    Function GetParsingData() As List(Of DataElement)
    Function GetRowCount() As Integer

    Sub LoadData()
End Interface
