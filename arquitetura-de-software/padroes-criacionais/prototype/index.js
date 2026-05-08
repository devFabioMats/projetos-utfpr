class ResumeTemplate {
  constructor(name, role, skills) {
    this.name = name;
    this.role = role;
    this.skills = skills;
  }

  clone() {
    return new ResumeTemplate(this.name, this.role, [...this.skills]);
  }
}

const baseResume = new ResumeTemplate("Default Name", "Software Developer", [
  "JavaScript",
  "SQL"
]);

const resumeForAlice = baseResume.clone();
resumeForAlice.name = "Alice";
resumeForAlice.skills.push("Node.js");

const resumeForBob = baseResume.clone();
resumeForBob.name = "Bob";
resumeForBob.skills.push("React");

console.log("Base resume:", baseResume);
console.log("Alice resume:", resumeForAlice);
console.log("Bob resume:", resumeForBob);
