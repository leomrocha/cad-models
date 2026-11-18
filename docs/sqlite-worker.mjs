import {search} from './engine.mjs';
self.onmessage = async ({data}) => {
  const {request, args} = data;
  try {
    self.postMessage({request, rows: await search('sqlite', ...args)});
  } catch (error) {
    self.postMessage({request, error: String(error)});
  }
};
