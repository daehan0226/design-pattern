import * as fs from "fs";
import { FileReader } from "./fileReader.js";

export class CsvFileReader extends FileReader {
  read(filename) {
    try {
      const data = fs.readFileSync(`./strategy/${filename}`, "utf8");
      return data;
    } catch (err) {
      console.log(err.message)
      return err.message;
    }
  }
}
