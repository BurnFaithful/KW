<%@ page import="java.util.ArrayList" %><%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-10-02
  Time: 오후 2:29
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta charset="UTF-8">
    <title>Add</title>
</head>
<body>
    <%
        request.setCharacterEncoding("UTF-8");
        String productName = request.getParameter("product");
        ArrayList productList = (ArrayList)session.getAttribute("productlist");
        if (productList == null)
        {
            productList = new ArrayList();
            session.setAttribute("productlist", productList);
        }
        productList.add(productName);
    %>
    <script>
        alert("<%=productName %>이(가) 추가되었습니다.");
        history.back();
    </script>
</body>
</html>
