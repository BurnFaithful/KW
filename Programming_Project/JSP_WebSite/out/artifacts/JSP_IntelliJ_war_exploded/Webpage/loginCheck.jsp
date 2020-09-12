<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="youngmin.web.UserDAO, java.io.PrintWriter" %>

<% request.setCharacterEncoding("UTF-8"); %>
<jsp:useBean id="user" class="youngmin.web.User" scope="page"/>
<jsp:setProperty name="user" property="id"/>
<jsp:setProperty name="user" property="password"/>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<% 
		UserDAO DAO = new UserDAO();
		int result = DAO.login(user.getId(), user.getPassword());
		PrintWriter script = response.getWriter();
		if (result == 1) // Success
		{
			script.println("<script>");
			script.println("alert('Login Success')");
			script.println("</script>");
		}
		else if (result == 0) // Fail
		{
			script.println("<script>");
			script.println("alert('Login Fail')");
			script.println("</script>");
		}
		else if (result == -1) // non-exist id
		{
			script.println("<script>");
			script.println("alert('non-exist ID')");
			script.println("</script>");
		}
		else
		{
			script.println("<script>");
			script.println("alert('database Error')");
			script.println("</script>");
		}
			
	%>
</body>
</html>