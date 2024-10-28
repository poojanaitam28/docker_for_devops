# Use an official OpenJDK image as a base
FROM openjdk:11

# Set the working directory
WORKDIR /app

# Copy the Java file to the Docker image
COPY GreetUser.java /app/

# Compile the Java program
RUN javac GreetUser.java

# Run the Java program
CMD ["java", "GreetUser"]

