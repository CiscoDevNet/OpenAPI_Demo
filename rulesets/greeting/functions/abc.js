export default input => {
    if (input !== "hello") {
      return [
        {
          message: 'Value must equal "hello".',
        },
      ];
    }
  };