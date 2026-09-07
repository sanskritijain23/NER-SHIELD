export const getRiskClassification = (score) => {
  if (score >= 0 && score <= 30) {
    return {
      level: "LOW",
      color: "text-green-500",
      bgColor: "bg-green-500",
      lightBgColor: "bg-green-50",
      borderColor: "border-green-200",
      action: "Continue routine monitoring.",
      mapColor: "green"
    };
  } else if (score >= 31 && score <= 60) {
    return {
      level: "MEDIUM",
      color: "text-yellow-500",
      bgColor: "bg-yellow-500",
      lightBgColor: "bg-yellow-50",
      borderColor: "border-yellow-200",
      action: "Increase monitoring of the location.",
      mapColor: "yellow"
    };
  } else if (score >= 61 && score <= 80) {
    return {
      level: "HIGH",
      color: "text-orange-500",
      bgColor: "bg-orange-500",
      lightBgColor: "bg-orange-50",
      borderColor: "border-orange-200",
      action: "Field inspection recommended.",
      mapColor: "orange"
    };
  } else {
    return {
      level: "CRITICAL",
      color: "text-red-600",
      bgColor: "bg-red-600",
      lightBgColor: "bg-red-50",
      borderColor: "border-red-200",
      action: "Immediate attention and field inspection recommended.",
      mapColor: "red"
    };
  }
};
