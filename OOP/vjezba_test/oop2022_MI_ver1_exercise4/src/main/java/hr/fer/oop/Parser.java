package hr.fer.oop;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.lang.Exception;

public class Parser {
	
	public static Reading parseInputString(String inputReadingString) throws ParseReadingException, IncorrectReadingFormatException, FormatException{
            Reading c;
            String[] x=inputReadingString.split(",");
	    if(x.length!=3) throw new IncorrectReadingFormatException(new Exception());
            return null; 
	}
	
	private static LocalDate parseDate (String dateA) throws FormatException{
		DateTimeFormatter dtf = DateTimeFormatter.ofPattern("MM-dd-yyyy");
		dtf = dtf.withLocale( Locale.GERMAN );
		LocalDate date = LocalDate.parse(dateA, dtf);
		
		return date;
	}

}
