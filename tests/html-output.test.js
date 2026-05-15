const fs = require("fs");

test("weekly_operating_review.html exists", () => {
  expect(
    fs.existsSync("docs/sample_weekly_operating_review.html")
  ).toBe(true);
});
