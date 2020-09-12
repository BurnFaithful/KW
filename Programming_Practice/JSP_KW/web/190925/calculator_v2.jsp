<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<% 
int result = 0;
String divideException = "";

if (request.getMethod().equals("POST"))
{
	String op = request.getParameter("operator");
	
	int left = Integer.parseInt(request.getParameter("left"));
	int right = Integer.parseInt(request.getParameter("right"));
	
	switch (op)
	{
		case "+":
			result = left + right;
			break;
		case "-":
			result = left - right;
			break;
		case "*":
			result = left * right;
			break;
		case "/":
			try
			{
				result = left / right;
			}
			catch (ArithmeticException e)
			{
				result = 0;
				divideException = "Divide By Zero.";
			}
			break;
	}
}
%>

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
</head>
<body>
	<h3>계산기를 씁시다.</h3>
	<hr>
	<form name=form1 method=post>
		<input type="text" name="left" width=200 size="5">
		<select name="operator">
			<option selected>+</option>
			<option>-</option>
			<option>*</option>
			<option>/</option>
		</select>
		
		<input type="text" name="right" width=200 size="5">
		<input type="submit" value="계산" name="B1">
		<input type="reset" value="다시입력" name="B2">
	</form>
	<hr>
	
	계산결과 : <%= result %><br>
	<%= divideException %>
</body>
</html>