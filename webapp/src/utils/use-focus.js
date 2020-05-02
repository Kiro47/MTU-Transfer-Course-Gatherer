import {useRef} from 'react';

export default () => {
  const ref = useRef(null);

  const setFocus = () => {
    if (ref.current) {
      ref.current.focus();
    }
  };

  return [ref, setFocus];
};
