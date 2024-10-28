# Use an official OpenJDK image as a base
FROM openjdk:11

# Set the working directory
WORKDIR /app

# Copy the Java file to the image
COPY TimeDisplay.java /app/

# Compile the Java program
RUN javac TimeDisplay.java

# Run the Java program
CMD ["java", "TimeDisplay"]

