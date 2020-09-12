<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-13
  Time: 오후 1:26
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <%@include file="file_header.jsp" %>
    <script src="../../js/page_func.js"></script>

    <title>위시리스트</title>
</head>
<body>
<%@include file="page_header.jsp" %>
<script>
    checkPage("${param.pageName}");
</script>

<%@include file="page_footer.jsp" %>
</body>
</html>
