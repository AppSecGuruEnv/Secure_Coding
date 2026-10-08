import java.io.FileInputStream;
import java.io.IOException;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import org.w3c.dom.Document;
import org.w3c.dom. Element;
import org.w3c.dom.NodeList;


class SimpleParser {

	public static void main(String[] args) throws IOException, ParserConfigurationException {
		if (args.length < 1) {
			System.out.println("Usage: SimpleParser XMLFILE");
			System.exit(-1);
			}

		String fileName = args[0];
		DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();

		FileInputStream XmlFile = new FileInputStream(fileName);
		DocumentBuilder docBuilder = docBuilderFactory.newDocumentBuilder();
		
		try {
			Document doc = docBuilder.parse(XmlFile);
			NodeList nList = doc.getElementsByTagName(doc.getDocumentElement().getNodeName());
			Element eElement = (Element) nList.item(0);
			System.out.println(eElement.getFirstChild().getTextContent());
		} catch (Exception ex) {
			System.out.println("Parse error: " + ex);
		}
	}
}
