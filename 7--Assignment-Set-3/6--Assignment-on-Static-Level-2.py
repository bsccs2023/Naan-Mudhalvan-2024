class Applicant:
    # Static variables
    __applicant_id_count = 1000
    __application_dict = {'A': 0, 'B': 0, 'C': 0}  # Keeps track of applications per job band

    def __init__(self, applicant_name):
        self.__applicant_id = None  # Initially None, will be assigned a value later
        self.__applicant_name = applicant_name
        self.__job_band = None

    # Getter methods for instance variables
    def get_applicant_id(self):
        return self.__applicant_id

    def get_applicant_name(self):
        return self.__applicant_name

    def get_job_band(self):
        return self.__job_band

    # Static method to access the application count dictionary
    @staticmethod
    def get_application_dict():
        return Applicant.__application_dict

    def generate_applicant_id(self):
        # Increment the static applicant ID counter and assign it to the applicant
        if Applicant.__applicant_id_count is not None:
            Applicant.__applicant_id_count += 1
            self.__applicant_id = Applicant.__applicant_id_count
        else:
            # Initialize the applicant ID count if it's None (which should never happen)
            Applicant.__applicant_id_count = 1001
            self.__applicant_id = Applicant.__applicant_id_count

    def apply_for_job(self, job_band):
        # Check if the applied job band is valid and has not reached the application limit
        if job_band in Applicant.__application_dict and Applicant.__application_dict[job_band] < 5:
            # Increment application count for the job band
            Applicant.__application_dict[job_band] += 1
            # Generate and assign applicant ID
            self.generate_applicant_id()
            # Assign the job band to the applicant
            self.__job_band = job_band
            return self.__applicant_id  # Return the applicant ID if successful
        else:
            return -1  # Return -1 if the job band is full or invalid

# Testing the implementation

# Create applicant objects
applicant1 = Applicant("Alice")
applicant2 = Applicant("Bob")
applicant3 = Applicant("Charlie")
applicant4 = Applicant("David")
applicant5 = Applicant("Eve")
applicant6 = Applicant("Frank")

# Apply for job bands and check results
applications = [
    (applicant1, "A"),
    (applicant2, "A"),
    (applicant3, "A"),
    (applicant4, "A"),
    (applicant5, "A"),  # This is the 5th application for job band "A"
    (applicant6, "A"),  # This should fail since the limit is reached
]

for applicant, job_band in applications:
    result = applicant.apply_for_job(job_band)
    if result != -1:
        print(f"Application successful! Applicant ID: {applicant.get_applicant_id()}, Name: {applicant.get_applicant_name()}, Job Band: {applicant.get_job_band()}")
    else:
        print(f"Application failed for {applicant.get_applicant_name()}. Job Band '{job_band}' is full.")

# Checking the application dictionary status
print("\nApplication status per job band:", Applicant.get_application_dict())