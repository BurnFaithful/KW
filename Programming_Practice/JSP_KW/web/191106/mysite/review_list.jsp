<%@ page import="youngmin.bbs.ReviewbbsDAO" %>
<%@ page import="youngmin.bbs.ReviewbbsDTO" %>
<%@ page import="java.util.ArrayList" %><%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-13
  Time: 오후 1:25
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <%@include file="file_header.jsp" %>
    <script src="../../js/page_func.js"></script>

    <title>리뷰 목록 페이지</title>
</head>
<body>
<%@include file="page_header.jsp" %>
<script>
    checkPage("${param.pageName}");
</script>

<div class="container">
    <div class="row">
        <table class="table table-striped" style="text-align: center; border: 1px solid #dddddd">
            <thead>
            <tr>
                <th style="background-color: #eeeeee; text-align: center;">번호</th>
                <th style="background-color: #eeeeee; text-align: center;">영화 제목</th>
                <th style="background-color: #eeeeee; text-align: center;">작성자</th>
                <th style="background-color: #eeeeee; text-align: center;">작성일</th>
            </tr>
            </thead>
            <tbody>
<%
    ArrayList<ReviewbbsDTO> bbsInfoList = new ReviewbbsDAO().getBBSList();
    for (ReviewbbsDTO reviewbbsInfo:bbsInfoList)
    {
%>
            <tr>
                <td><%= reviewbbsInfo.getReviewID() %></td>
                <td><a href="review_view.jsp?reviewID=<%= reviewbbsInfo.getReviewID()%>&pageName=Review_List"><%= reviewbbsInfo.getReviewTitle()%></a></td>
                <td><%= reviewbbsInfo.getWriterNickname()%></td>
                <td><%= reviewbbsInfo.getReviewDate()%></td>
            </tr>
<%
    }
%>
<%--            <tr>--%>
<%--                <td>1</td>--%>
<%--                <td><a href="#">다크나이트</a></td>--%>
<%--                <td>권영민</td>--%>
<%--                <td>2019-11-13</td>--%>
<%--            </tr>--%>
<%--            <tr>--%>
<%--                <td>2</td>--%>
<%--                <td><a href="#">어바웃 타임</a></td>--%>
<%--                <td>홍길동</td>--%>
<%--                <td>2019-11-19</td>--%>
<%--            </tr>--%>
<%--            <tr>--%>
<%--                <td>3</td>--%>
<%--                <td><a href="#">스파이더맨 2</a></td>--%>
<%--                <td>임꺽정</td>--%>
<%--                <td>2018-09-15</td>--%>
<%--            </tr>--%>
<%--            <tr>--%>
<%--                <td>4</td>--%>
<%--                <td><a href="#">우리는 동물원을 샀다</a></td>--%>
<%--                <td>성춘향</td>--%>
<%--                <td>2019-10-05</td>--%>
<%--            </tr>--%>
            </tbody>
        </table>
    </div>
</div>

<%@include file="page_footer.jsp" %>
</body>
</html>
