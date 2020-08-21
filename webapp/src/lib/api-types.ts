export interface APITransferCourse {
  id: number;
  course_id: string;
  course_name: string;
  course_subject: string;
  course_credits: string;
  transfer_course_credit: number;
  transfer_course_number: string;
  transfer_college: string;
  transfer_location: string;
}

export interface APIResult<ResultType> {
  count: number;
  next: string | null;
  previous: string | null;
  results: ResultType[];
}
