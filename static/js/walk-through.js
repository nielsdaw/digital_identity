$(document).ready(function () {
    // Instance the tour
    var tour = new Tour({
      steps: [
      {
        element: "#connect-profiles",
        title: "Connect profiles ",
        content: "Here you can connect your social media profiles."
      },
      {
        element: "#social-me",
        title: "Social Me",
        content: "Here you can view your Social Me, which is based on the information you provide on your connected social media profiles."
      },
      {
        element: "#dashboard",
        title: "Dashboard",
        content: "Here you can have a brief overview of your connected social media profiles."
      }
    ]});

    // Initialize the tour
    tour.init();

    // Start the tour
    tour.start();
});