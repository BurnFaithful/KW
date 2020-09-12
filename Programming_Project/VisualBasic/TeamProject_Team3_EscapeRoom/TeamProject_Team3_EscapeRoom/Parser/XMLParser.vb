Imports System.Xml
Imports System.Linq
Imports System.IO

Public MustInherit Class XMLParser
    Implements IParser

    Protected parsingData As New List(Of DataElement)

    Protected doc As XDocument

    Protected Sub ReadXMLData(xmlPath As String, xName As String)

        doc = XDocument.Load(Directory.GetParent(Application.StartupPath).Parent.FullName & "\" & xmlPath)

        Dim rootElement As XElement = doc.Root

        Dim dataCount As Integer = rootElement.Nodes.Count
        For i = 0 To dataCount - 1 ' Node Loop
            Dim dataElement = rootElement.Descendants(xName).ElementAt(i)

            Dim attributeCount As Integer = dataElement.Attributes().Count()
            Dim dataElementList As DataElement = New DataElement()
            For j = 0 To attributeCount - 1 ' Attribute Loop
                Dim dataAttribute = dataElement.Attributes().ElementAt(j)
                Dim pairData As DataItem = New DataItem

                pairData.key = dataAttribute.Name.ToString()
                pairData.value = dataAttribute.Value.ToString()

                dataElementList.dataList.Add(pairData)

#If DEBUG Then
                'Debug.WriteLine(pairData.key & " : " & pairData.value) ' 값 출력 확인
#End If
            Next j
            parsingData.Add(dataElementList)
        Next i
    End Sub

    Public Overridable Function FindElementByKey(key As String, value As String, ByRef element As DataElement) As Boolean Implements IParser.FindElementByKey
        Dim dataCount = parsingData.Count
        For i = 0 To dataCount - 1

            Dim attributeCount = parsingData(i).dataList.Count
            For j = 0 To attributeCount - 1
                Dim pairData As DataItem = parsingData(i).dataList(j)
                If pairData.key = key And pairData.value = value Then
                    element = parsingData(i)
                    Return True
                End If
            Next j
        Next i

        element = Nothing
        Return False
    End Function

    ' Data Parameter Add
    Public Overridable Function FindElementByKey(key As String, value As String, dataList As List(Of DataElement), ByRef element As DataElement) As Boolean Implements IParser.FindElementByKey

        Dim dataCount = dataList.Count
        For i = 0 To dataCount - 1

            Dim attributeCount = dataList(i).dataList.Count
            For j = 0 To attributeCount - 1
                Dim pairData As DataItem = dataList(i).dataList(j)
                If pairData.key = key And pairData.value = value Then
                    element = dataList(i)
                    Return True
                End If
            Next j
        Next i

        element = Nothing
        Return False
    End Function

    Public Overridable Function GetParsingData() As List(Of DataElement) Implements IParser.GetParsingData
        Return parsingData
    End Function

    Public Overridable Function GetRowCount() As Integer Implements IParser.GetRowCount
        Return doc.Root.Nodes.Count
    End Function

    Public MustOverride Sub LoadData() Implements IParser.LoadData

End Class
