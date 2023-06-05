'use strict';

module.exports = function (targetVal, opts) {

  // default to hello if no options specified
  let keyword = 'hello'
  if (opts.match) {
    keyword = opts.match
  }

  if (!targetVal.match(keyword)) {
    return [
      {
        message: `message must contain the keywoard '${keyword}'`
      }
    ];
  }
}