import { CsvFileReader } from "./csvFileReader.js";
import { JsonFileReader } from "./jsonFileReader.js";

const filename = process.argv[2];

// 입력된 파일에 따라 다른 전략(상호 교체 가능한)으로 파일 읽을 수 있다.
// read 이외의 기능이 많을때에는 각 객체에서 구현한다.
// 다른 파일 확장자을 읽는 기능이 요구될때 해당 객체를 추가해준다.
// 분기 처리는 팩토리 패턴을 이용해서 인스턴스를 받을 수 있다.
let fileReader;
if (filename.endsWith("json")) {
  fileReader = new JsonFileReader();
} else if (filename.endsWith("csv")) {
  fileReader = new CsvFileReader();
}

const data = fileReader.read(filename);
console.log(data)