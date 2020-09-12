Imports TeamProject_Team3_EscapeRoom

Public Class PropData
    Inherits XMLParser

    ' Singleton
    Private Sub New()

    End Sub

    Public Shared ReadOnly Property GetInstance As PropData
        Get
            Static Instance As PropData = New PropData()
            Return Instance
        End Get
    End Property
    ' Singleton

    Public Overrides Function FindElementByKey(key As String, value As String, ByRef element As DataElement) As Boolean
        Return MyBase.FindElementByKey(key, value, element)
    End Function

    Public Overrides Function FindElementByKey(key As String, value As String, dataList As List(Of DataElement), ByRef element As DataElement) As Boolean
        Return MyBase.FindElementByKey(key, value, dataList, element)
    End Function

    Public Overrides Function GetParsingData() As List(Of DataElement)
        Return MyBase.GetParsingData()
    End Function

    Public Overrides Function GetRowCount() As Integer
        Return MyBase.GetRowCount()
    End Function

    Public Overrides Sub LoadData()
        ReadXMLData("Data/PropData.xml", "Prop")
    End Sub

End Class
