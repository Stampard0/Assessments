<?xml version="1.0"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
    <table border="1">
      <tr bgcolor="firebrick">
        <th><font color="white">Title</font></th>
        <th><font color="white">Author</font></th>
        <th><font color="white">Publication Date</font></th>
      </tr>
      <xsl:for-each select="catalog/book">
	<xsl:sort select="title"/>
	<xsl:if test="pubdate &gt; 2005">
        <tr>
          <td><xsl:value-of select="title"/></td>
          <td><xsl:value-of select="author"/></td>
          <td><xsl:value-of select="pubdate"/></td>
        </tr>
	</xsl:if>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>